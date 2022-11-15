import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './App.css';
import { Tabs, Tab } from 'react-bootstrap';
import Table from './Table';

export const uid = () =>
  String(
    Date.now().toString(32) +
      Math.random().toString(16)
  ).replace(/\./g, '');

const API_URL = 'http://localhost:8000';

export const DataContext = React.createContext({});


const App = () => {
  const [currentSubject, setCurrentSubject] = useState('persons');
  const [data, setData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [perPage, setPerPage] = useState(10);
  const [countEntitys, setCountEntitys] = useState(0);
  const [loaded, setLoaded] = useState(false);
  const [sortBy, setSortBy] = useState('pk');
  const [filters, setFilters] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      setLoaded(false);
      const searchsString = Object.entries(filters).map(([key,value]) => `${key}=${value}`).join('*');
      const url = `${API_URL}/${currentSubject}/?page=${currentPage}&per=${perPage}&sortby=${sortBy}&filters=${searchsString}`;
      const response = await axios.get(url);
      console.log('------responsedDATA', response.data);
      setData(response.data.data);
      setLoaded(true);
      setCountEntitys(response.data.count);
      setCurrentPage(response.data.page);
    }
    
    fetchData();
  }, [currentSubject, currentPage, perPage, sortBy, filters])

  const renderPagination = () => {
    const pagesCount = Math.ceil(countEntitys / perPage);
    const pagesList = Array.from(Array(pagesCount + 1).keys()).slice(1);
    return (
      <>
        {pagesList.map((page) => (
        <span 
          className={currentPage === page ? 'selected-page' : 'pages'} 
          key={page}
          onClick={() => setCurrentPage(page)}>
          {` ${page}`}
        </span>
        ))}
      </>
    );
  };

  const renderSort = () => {
    return (
      <form>
        <label>
          Кол-во записей на страницу:
          <select value={perPage} onChange={(e) => setPerPage(e.target.value)}>
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="50">50</option>
            <option value="200">200</option>
            <option value="500">500</option>
          </select>
          {data[0] && <> Сортировать по:
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
            {Object.keys(data[0]).map((key) => <option key={key} value={key}>{key}</option>)}
          </select>
              </>}
        </label>
      </form>
    );
  };

  const handleSearch = (e) => {
    e.preventDefault();
    const key = e.target[0].name;
    const value = e.target[0].value;
    if (value) {
      const updatedFilters = {};
      updatedFilters[key] = value;
      setFilters({...filters, ...updatedFilters});
    } 
       else {
        const {...rest } = filters;
        delete rest[key];
        setFilters(rest);
       } 
  }

  const renderFilterForms = (entity) => {
    return (
    <tr><td></td>
      {Object.keys(entity).slice(1).map((key) => 
        <td key={uid()}>
          <form onSubmit={handleSearch}>
            <label>
              <input type="text" name={key} placeholder={filters[key]}/>
            </label>
            <input type="submit" value="Поиск" />
          </form>
        </td>)}
    </tr>
    );
  };

  const renderTableHead = (entity) => {
    return (
      <thead >
      <tr>
        {Object.keys(entity).map((key) => 
        <th key={uid()}>
          {key}<br />
        </th>)}
      </tr>
      {renderFilterForms(entity)}
      </thead>
      );
  };

  const content = (data.length === 0) ? 'Нет подходящих записей' : (
    <DataContext.Provider value={data}>
      Всего: <b>{countEntitys}</b>
      <br />
           Страницы: {renderPagination()}
           {renderSort()}
           {loaded && <table border="1">
              {renderTableHead(data[0])}
              <Table />
            </table>}
      Страницы: {renderPagination()}
    </DataContext.Provider>
  );

  const handleTab = (key) => {
    setCurrentSubject(key);
    setCurrentPage(1);
    setSortBy('pk');
    setFilters('');
  };


  return (
    <>
    <Tabs activeKey={currentSubject} onSelect={(key) => handleTab(key)}>
      <Tab eventKey="persons" title="Persons">
      </Tab>
      <Tab eventKey="cars" title="Cars">
      </Tab>
      </Tabs>
      {loaded ? content : <>Loading.....</>}
      </>
    );
};

export default App;
