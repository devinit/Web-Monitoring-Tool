import React, { useState } from 'react';
import { Table, Alert } from 'react-bootstrap';

export const ServerDashboard = ({ data, setAlertMessage }) => { // eslint-disable-line react/prop-types,max-len
  const [records, setRecords] = useState([]);

  React.useEffect(() => {
    try {
      window.fetch(`/records?server=${data.id}`)// eslint-disable-line react/prop-types
        .then((response) => response.json())
        .then((results) => {
          if (results) {
            setRecords(results);
          }
        })
        .catch((error) => {
          if (setAlertMessage) {
            setAlertMessage(error.message);
          }
        });
    } catch (error) {
      if (setAlertMessage) {
        setAlertMessage(error.message);
      }
    }
  }, []); // eslint-disable-line

  const renderRecord = (record, index) => (
    <tr key={index}>
      <td>{ record.key }</td>
      <td>{ record.value }</td>
      <td>{ new Date(record.created_on).toDateString() }</td>
    </tr>
  );

  if (records.length) {
    return (
      <Table>
        <tbody>
          { records.map(renderRecord) }
        </tbody>
      </Table>
    );
  }

  return <Alert variant="info">No Records Found</Alert>;
};

export default ServerDashboard;
