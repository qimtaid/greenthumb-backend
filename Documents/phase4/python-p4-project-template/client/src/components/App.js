import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import EventList from './components/EventList';
import EventForm from './components/EventForm';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route exact path="/" component={EventList} />
          <Route path="/add" component={EventForm} />
          <Route path="/edit/:id" component={EventForm} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
