import React, { Component } from "react";
import axios from 'axios';
import ClientTable from "./ClientTable";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
const API = '/api/client/';
//const DEFAULT_QUERY = 'redux';

class Clients extends Component {
  constructor(props) {
    super(props);

    this.state = {
        clients: [],
        isLoading: false,
        error: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });

    axios.get(API)
      .then(result => this.setState({
        clients: result.data,
        isLoading: false,
      }))
      .catch(error => this.setState({
        error,
        isLoading: false
      }));
  }

  render() {
      const { clients, isLoading, error } = this.state;
      console.log(clients)
      console.log(error)
      if (error) {
        return (<p>{error.message}</p>);
      }

      if (isLoading) {
        return (
        <div class="d-flex justify-content-center">
            <div class="spinner-border text-success" role="status">
            <span class="sr-only">Loading...</span>
            </div>
        </div>
        );
      }
    return (
    <div>
      <ClientTable data = {clients} />
    </div>
    );
  }
}
export default Clients;
