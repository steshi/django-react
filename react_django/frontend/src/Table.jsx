import React, {useContext} from "react";
import { uid, DataContext } from "./App";

const Table = () => {
	
	const data = useContext(DataContext);
	// console.log('---rendering table', data);
	const stringify_value = (value) => {
		if (!Array.isArray(value)) {
			return value;
		}
		const cars = value;
		return (
			<ul>
				{cars.map(({ model, number })=> (<li><b>model:</b> {model}  <b>number:</b> {number} </li>))}
			</ul>
		) 
	}

		return (
			<tbody>
				{data.map((item) => (
					<tr key={uid()}>
						{Object.values(item).map((value) => <td key={value}>{stringify_value(value)}</td> )}
					</tr>
				))}
			</tbody>				
		);
};

export default Table;