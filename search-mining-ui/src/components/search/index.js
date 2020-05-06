import { useAsyncAbortable } from "react-async-hook";

import * as React from "react";
import { useState } from "react";
import useConstant from "use-constant";
import AwesomeDebouncePromise from "awesome-debounce-promise";
import {
  Divider,
  Grid,
  Segment,
  Header,
  Container,
  Icon
} from "semantic-ui-react";

const API_SEARCH =
  "https://n55bunkzgh.execute-api.eu-west-1.amazonaws.com/prod/v1";
const API_SEARCH_PARAM = "search";

const searchEnginAPI = async (text, abortSignal) => {
  const result = await fetch(
    `${API_SEARCH}?${API_SEARCH_PARAM}=${encodeURIComponent(text)}`,
    {
      signal: abortSignal
    }
  );
  if (result.status !== 200) {
    throw new Error("bad status = " + result.status);
  }
  const response = await result.json();
  const responseCorrection = JSON.stringify(response).replace(
    /ranking score/g,
    "ranking_score"
  );
  return JSON.parse(responseCorrection).results;
};

const useSearchEngin = () => {
  // Handle the input text state
  const [inputText, setInputText] = useState("");

  // Debounce the original search async function
  const debouncedSearchEnginCall = useConstant(() =>
    AwesomeDebouncePromise(searchEnginAPI, 300)
  );

  const search = useAsyncAbortable(
    async (abortSignal, text) => {
      // If the input is empty, return nothing immediately (without the debouncing delay!)
      if (text.length === 0) {
        return [];
      }
      // Else we use the debounced api
      else {
        return debouncedSearchEnginCall(text, abortSignal);
      }
    },
    // Ensure a new request is made everytime the text changes (even if it's debounced)
    [inputText]
  );

  // Return everything needed for the hook consumer
  return {
    inputText,
    setInputText,
    search
  };
};

const SearchMining = () => {
  const { inputText, setInputText, search } = useSearchEngin();
  return (
    <Container textAlign="justified">
      <Divider />
      <input
        value={inputText}
        onChange={e => setInputText(e.target.value)}
        placeholder="Search mining"
        style={{
          marginTop: 20,
          padding: 10,
          border: "solid thin",
          borderRadius: 5,
          width: 300
        }}
      />
      <Divider />
      <Grid>
        <Grid.Column>
          <Segment>
            <div className="ui stacked segment">
              <p>
                Here below you see how the JavaScript code works and is
                returning example-results from our AI-model with name, path to
                directory, file format and ranking score. The ranking score is
                based on a deep learning neural network, a series of algorithms.
              </p>
            </div>
            <Divider />
            {search.loading && <div>...</div>}
            {search.error && <div>Error: {search.error.message}</div>}
            {search.result && (
              <div>
                <Header>Search Results: {search.result.length}</Header>
                <ul>
                  {search.result.map(
                    ({
                      document_name,
                      document_path,
                      document_type,
                      ranking_score
                    }) => (
                      <li key={document_name}>
                        <div className="ui relaxed divided list">
                          <div className="item">
                            <Icon
                              name={`file ${
                                document_type === "doc" ||
                                document_type === "docx"
                                  ? "word"
                                  : `pdf`
                              } outline`}
                              size="big"
                            />
                            <div className="content">
                              <div className="header">{document_name}</div>
                              <div className="description">{document_path}</div>
                              <div className="description">
                                <Icon name="chart line" size="large" /> Ranking
                                score: {ranking_score}
                              </div>
                            </div>
                          </div>
                        </div>
                      </li>
                    )
                  )}
                </ul>
              </div>
            )}
          </Segment>
        </Grid.Column>
      </Grid>
    </Container>
  );
};

const App = () => <SearchMining />;

export default App;
