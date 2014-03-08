'use strict';


// limited to strings, for now, b/c it uses `in` operator and object keys
function Set(elements) {
    var elems = {},
        self = this;
    elements.map(function(e) {
        self.add(e);
    });
    this._elements = elems;
}

Set.prototype.has = function(e) {
    return this._elements.hasOwnProperty(e);
};

Set.prototype.add = function(e) {
    this._elements[e] = 1;
};

Set.prototype.del = function(e) {
    delete this._elements[e];
};

Set.prototype.elems = function() {
    // I guess Object.getOwnPropertyNames vs. Object.keys doesn't really matter here
    return Object.keys(this._elements);
};

Set.prototype.minus = function(other) {
    function predicate(e) {
        return !other.has(e);
    }
    var elems = this.elems().filter(predicate);
    return new Set(elems);
};


module.exports = Set;
