import React, { Component } from "react";
import axios from 'axios';
import ProductTable from "./ProductTable";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
const API = '/api/product/';
//const DEFAULT_QUERY = 'redux';

class Potatoes extends Component {
  constructor(props) {
    super(props);

    this.state = {
        Potatoes: [],
        isLoading: false,
        error: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });

    axios.get(API)
      .then(result => this.setState({
        Potatoes: result.data,
        isLoading: false,
      }))
      .catch(error => this.setState({
        error,
        isLoading: false
      }));
  }

  render() {
      const { Potatoes, isLoading, error } = this.state;
      console.log(Potatoes)
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
      <ProductTable  data = {Potatoes} />
    </div>
    );
  }
}
export default Potatoes;
