import React, { Component } from 'react';
import logo from '../logo.svg';
import '../stylesheets/Header.css';


class Header extends Component {
  constructor(props){
    super();
    
  }

  componentDidMount(){
    this.props.getScore();
  }

  navTo(uri){
    window.location.href = window.location.origin + uri;
  }

  render() {
    return (
      <div className="App-header">
        <h1 onClick={() => {this.navTo('/qs')}}><img className="logo" src={logo}/>Udacitrivia</h1>
        <h2 onClick={() => {this.navTo('/qs')}}>List</h2>
        <h2 onClick={() => {this.navTo('/add')}}>Add</h2>
        <h2 onClick={() => {this.navTo('/play')}}>Play</h2>
        <h3 >Welcome {this.props.currentUser.username}</h3>
        <h3 >Your current Score:  {this.props.currentUser.score}</h3>       
        <h4 onClick={() => {this.navTo('/')}}>Logout</h4>
      </div>
    );
  }
}

export default Header;
