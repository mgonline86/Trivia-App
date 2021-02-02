import React, { Component } from 'react'

class NewCategory extends Component {
  state = {
    newCategory: '',
  }

  getInfo = (event) => {
    event.preventDefault();
    this.props.addCategory(this.state.newCategory)
  }

  handleInputChange = () => {
    this.setState({
      newCategory: this.search.value
    })
  }

  flipVisibility() {
    this.setState({visibleAnswer: !this.state.visibleAnswer});
  }

  render() {
    return (
      <React.Fragment>
        <div className="button" onClick={() => this.flipVisibility()}>
          {this.state.visibleAnswer ? 'Cancel' : '+ Add Category'}
        </div>
        <div className="answer-holder">
          <div style={{"visibility": this.state.visibleAnswer ? 'visible' : 'hidden'}}>
            <form onSubmit={this.getInfo}>
              <input placeholder="New Category..." ref={input => this.search = input} onChange={this.handleInputChange} required/>
              <input type="submit" value="Add" className="button"/>
            </form>
          </div>
        </div>
        <br></br>
      </React.Fragment>
    )
  }
}

export default NewCategory
