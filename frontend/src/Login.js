import React, { Component } from "react";
import {Form, Button, Card} from "react-bootstrap"

class Login extends Component {
  render() {
    return (
          <Card style={{ width: '50rem' }} bg="light" variant="dark"  >
          <Card.Body>
            <Card.Text>
                <Form>
                  <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                    <Form.Text className="text-muted">
                      We'll n ever share your email with anyone else.
                    </Form.Text>
                  </Form.Group>

                  <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                  </Form.Group>
                  <Form.Group controlId="formBasicChecbox">
                    <Form.Check type="checkbox" label="Remember Me" />
                  </Form.Group>
                  <Button variant="primary" type="submit">
                    Submit
                  </Button>
                </Form>
            </Card.Text>
          </Card.Body>
        </Card>
    );
  }
}

export default Login;