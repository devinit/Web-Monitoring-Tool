import React, { useState, useEffect } from 'react';
import Card from 'react-bootstrap/Card'
import Form from 'react-bootstrap/Form'
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'
import Moment from 'react-moment';


const ViewUser = ({user}) => {
// email	""
// first_name	""
// id	1
// is_superuser	true
// last_name	""
// username	"dave"
// date_joined	"2019-11-12T09:32:28.960Z"
// is_active	true
// last_login	"2019-11-13T21:50:38.724Z"

  return (
    <Form>
      <Form.Group as={Row} controlId="formPlaintextEmail">
        <Form.Label column sm="2">
          Username
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.username} />
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
          Admin
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.is_superuser} />
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

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Last Login
        </Form.Label>
        <Col sm="10" style={{ margin: '10px 0 0' }}>
          <Moment format="ddd Do MMMM, YYYY">{user.last_login}</Moment>
        </Col>
      </Form.Group>

      <Form.Group as={Row} controlId="formPlaintextPassword">
        <Form.Label column sm="2">
          Active
        </Form.Label>
        <Col sm="10">
          <Form.Control plaintext readOnly defaultValue={user.is_active} />
        </Col>
      </Form.Group>

    </Form>
  );
};

export { ViewUser as default, ViewUser };
