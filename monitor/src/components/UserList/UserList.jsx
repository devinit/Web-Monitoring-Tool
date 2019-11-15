import React, { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button'
import ButtonGroup from 'react-bootstrap/ButtonGroup'
import Moment from 'react-moment';
import { Popup } from '../Popup'

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [show, setShow] = useState();

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

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
      <td><Moment format="ddd Do MMMM, YYYY">{user.date_joined}</Moment></td>
      <td>{user.is_superuser ? "Yes" : "No"}</td>
      <td>
          <ButtonGroup aria-label="Basic example">
            <Button variant="info" onClick={handleShow}>View</Button>
            <Button variant="success">Edit</Button>
            <Button variant="danger">Delete</Button>
          </ButtonGroup>
      </td>
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
            <th>Manage</th>
          </tr>
        </thead>
        <tbody>
          {users.map(renderUser)}
        </tbody>
      </Table>
      <Popup popUpState={show} closePopup={handleClose}/>
      </div>
    </>
  );
};

export { UserList as default, UserList };
