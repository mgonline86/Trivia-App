import React, { Component } from 'react';
import '../stylesheets/Question.css';

const starArray = [5,4,3,2,1]
const cats=['Science','Art','Geography','History','Entertainment','Sports']

class Question extends Component {
  constructor(){
    super();
    this.state = {
      visibleAnswer: false
    }
  }


  flipVisibility() {
    this.setState({visibleAnswer: !this.state.visibleAnswer});
  }

  render() {
    const { question, answer, category, difficulty, rating } = this.props;
    return (
      <div className="Question-holder">
        <div className="Question">{question}</div>
        <div className="Question-status">
          <img className="category" src={cats.includes(category)?`${category}.svg`:'lightbulb.svg'}/>
          <div className="difficulty">Difficulty: {difficulty}</div>
          <div className="rating">
            {starArray.map(num => (
              <div
                key={num}
                onClick={() => this.props.questionAction('PATCH',num)}
                className={`star ${rating >= num ? 'active':''}`}
              />
            ))}
          Rating: </div>
          <img src="delete.png" className="delete" onClick={() => this.props.questionAction('DELETE')}/>
          
        </div>
        <div className="show-answer button"
            onClick={() => this.flipVisibility()}>
            {this.state.visibleAnswer ? 'Hide' : 'Show'} Answer
          </div>
        <div className="answer-holder">
          <span style={{"visibility": this.state.visibleAnswer ? 'visible' : 'hidden'}}>Answer: {answer}</span>
        </div>
      </div>
    );
  }
}

export default Question;
