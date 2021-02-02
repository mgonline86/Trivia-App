import React, { Component } from 'react';
import $ from 'jquery';
import logo from '../logo.svg';
import '../stylesheets/Login.css';
import '../stylesheets/Question.css';

class Login extends Component {

  constructor(){
    super();
    this.state = {
      username: '',
      password: '',
      correct_password: false,
      status:false
    }
  }

  navTo(uri){

      window.location.href = window.location.origin + uri;

    
  }

  userEval(uri){
    if (this.state.correct_password===true) {
      this.navTo(uri);
    } else {
      document.getElementById("Login-fail").className = "visible";
    } 
    
  }

  submitUser = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/login', 
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          correct_password: result.correct_password
        })
        return;
      },
      error: (error) => {
        console.log('Unable to Login')
        return;
      }
    })
  }

  guestUser = (event) => {
    event.preventDefault();
    $.ajax({
      url: '/login', 
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        username: 'Guest',
        password: 'Guest'
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        this.setState({
          correct_password: result.correct_password
        })
        return ;
      },
      error: (error) => {
        console.log('Unable to Login')
        return;
      }
    })
  }

  resetStatus = () => {
    $.ajax({
      url: '/status', 
      type: "POST",
      crossDomain: true,
      success: (result) => {
        console.log('Reset Status success')
        return;
      },
      error: (error) => {
        console.log('Unable to Reset Status')
        return;
      }
    })
  }  

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value})
  }
  componentDidMount(){
    this.resetStatus();
  }
  render() {
    return (
      <div className="App-login">
        <form className="form-view" id="user-login" onSubmit={this.submitUser}>
        <div><img className="logo-login" src={logo}/></div>
          <div id="welcome">Welcome to Udacitrivia</div>
          <label>
            Username:
            <input type="text" name="username" onChange={this.handleChange} required/>
          </label>
          <label>
            Password:
            <input type="text" name="password" onChange={this.handleChange} required/>
          </label>
          <span className="hidden" id="Login-fail">Incorrect Password</span>
          <input type="submit" className="button" value="Login" onClick={() =>setTimeout(() => {this.userEval('/main')},500)}/>
          <div className="anchor"><a href="/register">Register New User</a></div>
        </form>
        <form className="form-view" id="user-login" onSubmit={this.guestUser}>
        <input type="submit" className="button" value="Enter as Guest" onClick={() => {this.navTo('/main')}}/>
        </form>
      </div>
    );
  }
}

export default Login;
