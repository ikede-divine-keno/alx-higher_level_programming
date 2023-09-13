#!/usr/bin/node
// A Rectangle class

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    for (j = 0; j < this.height; j++) {
      let varRect = '';
      for (i = 0; i < this.width; i++) {
        varRect += 'X';
      }
      console.log(varRect);
    }
  }

  rotate () {
    let a = this.width;
    let b = this.height;

    this.width = b;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
