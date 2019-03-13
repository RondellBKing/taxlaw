 // frontend/src/components/Modal.js

    import React, { Component } from "react";
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Price Entry </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="price">Price</Label>
                  <Input
                    type="text"
                    name="price"
                    value={this.state.activeItem.price}
                    onChange={this.handleChange}
                    placeholder="Enter price price"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="client_id">Cient ID</Label>
                  <Input
                    type="text"
                    name="client_id"
                    value={this.state.activeItem.client_id}
                    onChange={this.handleChange}
                    placeholder="Enter Client ID"
                  />
                </FormGroup>
                <FormGroup check>
                  <Label for="validated">
                    <Input
                      type="checkbox"
                      name="validated"
                      checked={this.state.activeItem.completed}
                      onChange={this.handleChange}
                    />
                    Completed
                  </Label>
                </FormGroup>
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Save
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }