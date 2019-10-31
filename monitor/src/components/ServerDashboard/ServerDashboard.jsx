import React from 'react';
import { Table } from 'react-bootstrap';

const ServerDashboard = ({ data }) => { // eslint-disable-line react/prop-types
  console.log(data);
  const [records, setRecords] = React.useState([]);
  React.useEffect(() => {
    // TODO: fetch records here
    setRecords([
      {
        key: 'mem_free',
        value: '6615460',
        created_on: '2019-10-30T10:24:24.781Z',
      },
      {
        key: 'cpu',
        value: '80',
        created_on: '2019-10-31T10:24:24.781Z',
      },
    ]);
  }, []);

  const renderRecord = (record, index) => (
    <tr key={index}>
      <td>{ record.key }</td>
      <td>{ record.value }</td>
      <td>{ new Date(record.created_on).toDateString() }</td>
    </tr>
  );

  return (
    <Table>
      <tbody>
        { records.map(renderRecord) }
      </tbody>
    </Table>
  );
};

export { ServerDashboard as default, ServerDashboard };
