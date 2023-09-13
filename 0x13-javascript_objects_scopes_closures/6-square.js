#!/usr/bin/node

// A Rectangle class
/**
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
    const a = this.width;
    const b = this.height;

    this.width = b;
    this.height = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
**/
// A Square class

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let varSqua = '';
      if (c) {
        for (let j = 0; j < this.size; j++) {
          varSqua += c;
	}
      }
      else {
        for (let j = 0; j < this.size; j++) {
          varSqua += 'X';
        }
      }
      console.log(varSqua);
    }
  }
}

// module.exports = Rectangle;
module.exports = Square;
