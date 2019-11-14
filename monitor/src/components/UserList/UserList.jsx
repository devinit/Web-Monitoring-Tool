import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table'
import { Accordion, Card, Alert } from 'react-bootstrap';
import { ServerDashboard } from '../ServerDashboard';
import { ServerQueryForm } from '../ServerQueryForm';

const UserList = () => {
  const [servers, setServers] = useState([]);
  const [alertMessage, setAlertMessage] = useState('');
  useEffect(() => {
    try {
      window.fetch('/users_list')
        .then((response) => response.json())
        .then((results) => {
          if (results) {
            setServers(results);
          }
        })
        .catch((error) => setAlertMessage(error.message));
    } catch (error) {
      setAlertMessage(error.message);
    }
  }, []);
  const renderServer = (server, index) => (
    <tr key={index}>
      <td>{index + 1}</td>
      <td>{server.username}</td>
      <td>{server.date_joined}</td>
      <td>{server.is_superuser ? "Yes" : "No"}</td>
    </tr>
  );

  return (
    <>
      <div>
      <h3>Users</h3>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Username</th>
            <th>Date Joined</th>
            <th>Is Admin</th>
          </tr>
        </thead>
        <tbody>
          {servers.map(renderServer)}
        </tbody>
      </Table>
      </div>
    </>
  );
};

export { UserList as default, UserList };
