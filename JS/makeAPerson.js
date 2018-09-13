  var Person = function(str) {
    // Complete the method below and implement the others similarly
    firstName = str.split(" ")[0];
    lastName = str.split(" ")[1];

    this.getFirstName = function() {
      return firstName;
    }
    this.getLastName = function() {
      return lastName;
    }
    this.getFullName = function() {
      return `${firstName} ${lastName}`
    }
    this.setFirstName = function(first) {
      firstName = first
    }
    this.setLastName = function(last) {
      lastName = last
    }
    this.setFullName = function(firstAndLast) {
      firstName = firstAndLast.split(" ")[0];
      lastName = firstAndLast.split(" ")[1]
    }
  }
  var bob = new Person('Bob Ross');
  bob.getFirstName();
