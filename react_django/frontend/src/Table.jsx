import React, {useContext} from "react";
import { uid, DataContext } from "./App";

const Table = () => {
	
	const data = useContext(DataContext);
	// console.log('---rendering table', data);
		return (
			<tbody>
				{data.map((item) => (
					<tr key={uid()}>
						{Object.values(item).map((value) => <td key={uid()}>{value}</td> )}
					</tr>
				))}
			</tbody>				
		);
};

export default Table;