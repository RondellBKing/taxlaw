import React, { Component } from "react";
import {Card} from "react-bootstrap"
class Contact extends Component {
  render() {
    return (
      <div>
          <Card>
          <Card.Body>
            <Card.Title>Questions?</Card.Title>
            <Card.Text>
                Feel free to email all inquires.
            </Card.Text>
            <Card.Link href="mailto:RondellBKing@gmail.com">RondellBKing@gmail.com</Card.Link>
          </Card.Body>
        </Card>
      </div>
    );
  }
}

export default Contact;
