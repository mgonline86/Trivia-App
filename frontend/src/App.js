import React, { Component } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom'

// import logo from './logo.svg';
import './stylesheets/App.css';
import FormView from './components/FormView';
import QuestionView from './components/QuestionView';
import Header from './components/Header';
import QuizView from './components/QuizView';
import Login from './components/Login';
import Register from './components/Register';
import $ from 'jquery';

class App extends Component {
  state={
    currentUser: {},
    userScore: 0
  }
  getScore=()=>{
    $.ajax({
      url: `/users`,
      type: "GET",
      success: (result) => {
        this.setState({ currentUser: result.currentUser })
        return;
      },
      error: (error) => {
        alert('Unable to load User. Please try your request again')
        return;
      }
    }) 
  }


  render() {
    return (
    <div className="App">
      <Router>
        <Switch>      
          <Route path="/" exact component={Login}  />
          <Route path="/register" exact component={Register}  />
          <Router>
          <Header 
            path
            currentUser={this.state.currentUser}
            userScore={this.state.userScore}
            getScore = {this.getScore} 
          />
            <Switch>
              <Route path="/qs" exact component={QuestionView} />
              <Route path="/add" component={FormView} />
              <Route path="/play" render={props => <QuizView getScore = {this.getScore} />} />
              <Route component={QuestionView} />
            </Switch>
          </Router>
        </Switch>
      </Router>
    </div>
  );

  }
}

export default App;
