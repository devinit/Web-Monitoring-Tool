import React from 'react';
import { Accordion, Button, Card } from 'react-bootstrap';

const Servers = () => (
  <Accordion defaultActiveKey="0">
    <Card>
      <Card.Header>
        <Accordion.Toggle as={Button} variant="link" eventKey="0">
            Server 101
        </Accordion.Toggle>
      </Card.Header>
      <Accordion.Collapse eventKey="0">
        <Card.Body>Hello! I am the body</Card.Body>
      </Accordion.Collapse>
    </Card>
    <Card>
      <Card.Header>
        <Accordion.Toggle as={Button} variant="link" eventKey="1">
            Server 102
        </Accordion.Toggle>
      </Card.Header>
      <Accordion.Collapse eventKey="1">
        <Card.Body>Hello! I am another body</Card.Body>
      </Accordion.Collapse>
    </Card>
  </Accordion>
);

export { Servers as default, Servers };
