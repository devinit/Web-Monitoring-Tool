import React, { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Moment from 'react-moment';
import Editable from 'react-bootstrap-editable'
import qs from 'qs'
import axios from 'axios'


const ViewUser = ({user}) => {

  const editUsername = (username) => {
    const requestBody = {
      'username': username,
      'userid': user.id
    }

    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }

    axios.post('http://localhost:8090/users_update', qs.stringify(requestBody), config)
    .then((result) => {
      console.log("success"+JSON.stringify(data)); // JSON-string from `response.json()` call
    })
    .catch((err) => {
      // Do somthing
    });
  };

  return (
    <Form>
      <Form.Group as={Row} controlId="formPlaintextEmail">
        <Form.Label column sm="2">
          Username
        </Form.Label>
        <Col sm="10" style={{ margin: '7px 0 0' }}>
          <Editable
            alwaysEditing={false}
            disabled={false}
            editText="Edit"
            initialValue={user.username}
            isValueClickable={false}
            mode="inline"
            onSubmit={editUsername}
            placement="top"
            showText
            type="textfield"
            validate={(value) => {
              if(value.length <= 0){
                  return "Username is required"
              }
            }}
          />
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Firstname
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.first_name} />
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Lastname
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.last_name} />
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Email
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.email} />
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Joined
        </Form.Label>
        <Col sm="10" style={{ margin: '10px 0 0' }}>
          <Moment format="ddd Do MMMM, YYYY">{user.date_joined}</Moment>
        </Col>
      </Form.Group>

    </Form>
  );
};

export { ViewUser as default, ViewUser };
