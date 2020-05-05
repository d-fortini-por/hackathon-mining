import _ from "lodash";
import faker from "faker";
import React, { Component } from "react";
import {
  Divider,
  Grid,
  Segment,
  Search,
  Header,
  Container,
  Icon
} from "semantic-ui-react";
import GoogleMapReact from "google-map-react";

const initialState = { isLoading: false, results: [], value: "" };
const API_SEARCH =
  "https://n55bunkzgh.execute-api.eu-west-1.amazonaws.com/prod/v1";
const API_SEARCH_PARAM = "search";
const source = _.times(5, () => ({
  document_name: faker.system.fileName(),
  document_path: faker.system.filePath(),
  document_type: faker.system.commonFileExt(),
  ranking_score: faker.random.number()
}));
const AnyReactComponent = ({ text }) => <div>{text}</div>;
const defaultMap = {
  center: {
    lat: 50.9375,
    lng: 6.9603
  },
  zoom: 11
};

const resultRenderer = ({
  document_name,
  document_path,
  document_type,
  ranking_score
}) => (
  <div class="ui relaxed divided list">
    <div class="item">
      <Icon
        name={`file ${
          document_type === "doc" || document_type === "docx" ? "word" : `pdf`
        } outline icon`}
        size="big"
      />
      <div class="content">
        <a class="header">{document_name}</a>
        <div class="description">{document_path}</div>
        <div class="description">
          <Icon name="chart line" size="large" /> Ranking score: {ranking_score}
        </div>
      </div>
    </div>
  </div>
);

export default class SearchComponent extends Component {
  // Initialize state in constructor,
  // Or with a property initializer.
  state = initialState;

  static getDerivedStateFromProps(props, state) {
    return state;
  }

  handleResultSelect = (e, { result }) =>
    this.setState({ value: result.title });

  handleSearchChange = (e, { value }) => {
    this.setState({ isLoading: true, value });
    setTimeout(() => {
      if (this.state.value.length < 1) return this.setState(initialState);

      //const re = new RegExp(_.escapeRegExp(this.state.value), "i");
      //const isMatch = result => re.test(result.document_name);
      const isMatch = this.search(value);

      this.setState({
        isLoading: false,
        results: this.search(value)
      });
    }, 300);
  };

  async search(value = null) {
    if (value === "") {
      this.setState({ results: [] });
      return;
    }

    let response;
    try {
      response = await fetch(`${API_SEARCH}?${API_SEARCH_PARAM}=${value}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      });
    } catch (error) {
      console.log("failed to GET stats:", error);
      return;
    }

    let data;
    try {
      data = await response.json();
    } catch (error) {
      console.log("failed to parse response as JSON:", error);
      return;
    }

    this.setState({ results: data });
  }

  render() {
    const { isLoading, value, results } = this.state;

    return (
      <Container textAlign="justified">
        <Grid columns={2}>
          <Grid.Column>
            <Divider />
            <Search
              input={{ icon: "search", iconPosition: "left" }}
              loading={isLoading}
              onResultSelect={this.handleResultSelect}
              onSearchChange={_.debounce(this.handleSearchChange, 500, {
                leading: true
              })}
              results={results}
              resultRenderer={resultRenderer}
              value={value}
              {...this.props}
            />
            <Divider />
            <Container style={{ width: "100%", height: "400px" }}>
              {/* <GoogleMapReact
                bootstrapURLKeys={{
                  key: "AIzaSyDBCUAspjbDGyD-AA8sVQuUukeHr8YEUpQ"
                }}
                defaultCenter={defaultMap.center}
                defaultZoom={defaultMap.zoom}
              >
                <AnyReactComponent
                  lat={59.955413}
                  lng={30.337844}
                  text="My Marker"
                />
              </GoogleMapReact> */}
            </Container>
          </Grid.Column>
          <Grid.Column>
            <Segment>
              <Header>State</Header>
              <pre style={{ overflowX: "auto" }}>
                {JSON.stringify(this.state, null, 2)}
              </pre>
            </Segment>
          </Grid.Column>
        </Grid>
      </Container>
    );
  }
}
