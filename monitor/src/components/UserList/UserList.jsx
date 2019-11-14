import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table'

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    try {
      window.fetch('/users_list')
        .then((response) => response.json())
        .then((results) => {
          if (results) {
            setUsers(results);
          }
        })
        .catch((error) => setAlertMessage(error.message));
    } catch (error) {
      setAlertMessage(error.message);
    }
  }, []);

  const renderUser = (user, index) => (
    <tr key={index}>
      <td>{index + 1}</td>
      <td>{user.username}</td>
      <td>{user.date_joined}</td>
      <td>{user.is_superuser ? "Yes" : "No"}</td>
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
          {users.map(renderUser)}
        </tbody>
      </Table>
      </div>
    </>
  );
};

export { UserList as default, UserList };
