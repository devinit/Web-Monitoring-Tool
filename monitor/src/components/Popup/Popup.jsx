import React, { useState, useEffect } from 'react';
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import { ViewUser } from '../ViewUser'


const Popup = ({userObject, popUpState, closePopup}) => {

  return (
    <>
      <Modal show={popUpState} onHide={closePopup}>
        <Modal.Header closeButton>
        <Modal.Title>User Details for {userObject.username}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <ViewUser user={userObject} />
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={closePopup}>
            Close
          </Button>
          <Button variant="primary" onClick={closePopup}>
            Ok
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export { Popup as default, Popup };
