import React, { useState, useEffect } from 'react';
import { Accordion, Card, Alert } from 'react-bootstrap';
import { ServerDashboard } from '../ServerDashboard';
import { ServerQueryForm } from '../ServerQueryForm';

const Servers = () => {
  const [servers, setServers] = useState([]);
  const [alertMessage, setAlertMessage] = useState('');
  useEffect(() => {
    try {
      window.fetch('/servers/')
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
    <Card key={index}>
      <Card.Header>
        <Accordion.Toggle as={Card.Title} variant="link" eventKey={index}>
          {`${server.ip} - ${server.description}`}
        </Accordion.Toggle>
      </Card.Header>
      <Accordion.Collapse eventKey={index}>
        <Card.Body>
          <ServerQueryForm serverID={server.id} setAlertMessage={setAlertMessage} />
          <ServerDashboard data={server} setAlertMessage={setAlertMessage} />
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  );

  return (
    <>
      <Alert variant="danger" show={!!alertMessage} dismissible onClose={() => setAlertMessage('')}>
        { alertMessage }
      </Alert>
      <Accordion defaultActiveKey="0" className="monitored-servers">
        {servers.map(renderServer)}
      </Accordion>
    </>
  );
};

export { Servers as default, Servers };
