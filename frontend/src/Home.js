import React, {Component } from "react";
import {Card, CardGroup, Dropdown} from "react-bootstrap";
import axios from 'axios';

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

// Bloomberg Api
const API = 'https://newsapi.org/v2/top-headlines?' +
          'country=us&' +
          'apiKey=366826fe46a044e6ac9ad2124d36f4eb';

class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {
        news: [],
        isLoading: false,
        error: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });

    axios.get(API)
      .then(result => this.setState({
        news: result.data.articles,
        isLoading: false,
      }))
      .catch(error => this.setState({
        error,
        isLoading: false
      }));
  }

  render() {
  const { news, isLoading, error } = this.state;
    return (
      <div>
<CardGroup>
  <Card>
    <Card.Body>
      <Card.Title>Bloomberg Feed</Card.Title>
      <Card.Text>
        In this card, we have the newsapi, to get
        Live Data fro Bloomberg.
        This functionality is under construction
      </Card.Text>
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
  <Card>
    <Card.Body>
      <Card.Title>Pricing Updates</Card.Title>
      <Card.Text>
         In this page we can put Pricing updates received
         in real time.
      </Card.Text>
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
  <Card>
    <Card.Body>
      <Card.Title>Client Updates</Card.Title>
      <Card.Text>
        We can place Client Updates in this pane.
      </Card.Text>
    </Card.Body>
    <Card.Footer>
      <small className="text-muted">Last updated 3 mins ago</small>
    </Card.Footer>
  </Card>
</CardGroup>;
      </div>
    );
  }
}
export default Home;
