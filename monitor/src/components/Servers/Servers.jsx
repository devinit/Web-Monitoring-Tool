import React from 'react';
import { Accordion, Button, Card } from 'react-bootstrap';
import { ServerDashboard } from '../ServerDashboard';

const Servers = () => {
  const [servers, setServers] = React.useState([]);
  React.useEffect(() => {
    // TODO: fetch servers here
    setServers([
      {
        id: 1,
        ip: '172.18.0.1',
        description: "Alex's Laptop",
        domains: [],
      },
      {
        id: 2,
        ip: '172.18.0.2',
        description: "David's Laptop",
        domains: [],
      },
    ]);
  }, []);
  const renderServer = (server, index) => (
    <Card key={index}>
      <Card.Header>
        <Accordion.Toggle as={Button} variant="link" eventKey={index}>
          { `${server.ip} - ${server.description}` }
        </Accordion.Toggle>
      </Card.Header>
      <Accordion.Collapse eventKey={index}>
        <Card.Body>
          <ServerDashboard data={server} />
        </Card.Body>
      </Accordion.Collapse>
    </Card>
  );

  return (
    <Accordion defaultActiveKey="0" className="monitored-servers">
      { servers.map(renderServer) }
    </Accordion>
  );
};

export { Servers as default, Servers };
