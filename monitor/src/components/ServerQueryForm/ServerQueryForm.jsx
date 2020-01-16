import { Formik } from 'formik';
import PropTypes from 'prop-types';
import React, { useState } from 'react';
import {
  Button, Col, Form, FormGroup, FormLabel, Row,
} from 'react-bootstrap';
import { Dropdown } from 'semantic-ui-react';

const initialValues = { query: '', method_arg: '' };
const availableQueries = [
  { value: 'query_timestamp_uptodate', text: 'Is server responding' },
  { value: 'query_free_memory_percent', text: 'Percentage free memory' },
  { value: 'query_pid', text: 'Process ID' },
  { value: 'query_docker_id', text: 'Docker ID' },
  { value: 'query_generic', text: 'Generic' },
];

export const ServerQueryForm = ({ setAlertMessage, serverID }) => {
  const [value, setValue] = useState('');
  const [valid, setValid] = useState(false);
  const [selectedQuery, setSelectedQuery] = useState('');

  const onSuccess = (data) => {
    try {
      window.fetch(`/query?server=${serverID}&query=${selectedQuery}&method_arg=${data.method_arg}`)
        .then((response) => response.json())
        .then((result) => {
          if (result) {
            setValue(result);
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
    setValue('');
  };

  const onSelectQuery = (event, data) => {
    if (data && data.value) {
      setSelectedQuery(data.value);
      setValid(true);
    } else if (valid) {
      setValid(false);
    }
  };

  return (
    <Formik initialValues={initialValues} onSubmit={onSuccess}>
      {
        ({ handleChange, handleSubmit }) => (
          <Form className="form" noValidate onSubmit={handleSubmit}>
            <Row>
              <FormLabel className="col-sm-1 col-form-label" style={{ maxWidth: '3%' }}>Query</FormLabel>
              <Col md={8}>
                <Row>
                  <Col md={4}>
                    <FormGroup>
                      <Dropdown
                        placeholder="Select Query"
                        fluid
                        selection
                        options={availableQueries}
                        onChange={onSelectQuery}
                      />
                    </FormGroup>
                  </Col>
                  <Col md={4}>
                    <FormGroup className="bmd-form-group" style={{ margin: '5px 0 0' }}>
                      <Form.Control name="method_arg" onChange={handleChange} placeholder="Query Argument" />
                    </FormGroup>
                  </Col>
                  <Col md={2}>
                    <Button className="btn-rose" type="submit" disabled={!valid}>Execute</Button>
                  </Col>
                  <Col md={2}>
                    <FormLabel className="h4 col-form-label">{ value }</FormLabel>
                  </Col>
                </Row>
              </Col>
            </Row>
          </Form>
        )
      }
    </Formik>
  );
};

ServerQueryForm.propTypes = {
  serverID: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
  ]),
  setAlertMessage: PropTypes.func,
};

ServerQueryForm.defaultProps = {
  serverID: '',
  setAlertMessage: undefined,
};

export default ServerQueryForm;
