"use strict";

function _regenerator() { /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/babel/babel/blob/main/packages/babel-helpers/LICENSE */ var e, t, r = "function" == typeof Symbol ? Symbol : {}, n = r.iterator || "@@iterator", o = r.toStringTag || "@@toStringTag"; function i(r, n, o, i) { var c = n && n.prototype instanceof Generator ? n : Generator, u = Object.create(c.prototype); return _regeneratorDefine2(u, "_invoke", function (r, n, o) { var i, c, u, f = 0, p = o || [], y = !1, G = { p: 0, n: 0, v: e, a: d, f: d.bind(e, 4), d: function d(t, r) { return i = t, c = 0, u = e, G.n = r, a; } }; function d(r, n) { for (c = r, u = n, t = 0; !y && f && !o && t < p.length; t++) { var o, i = p[t], d = G.p, l = i[2]; r > 3 ? (o = l === n) && (u = i[(c = i[4]) ? 5 : (c = 3, 3)], i[4] = i[5] = e) : i[0] <= d && ((o = r < 2 && d < i[1]) ? (c = 0, G.v = n, G.n = i[1]) : d < l && (o = r < 3 || i[0] > n || n > l) && (i[4] = r, i[5] = n, G.n = l, c = 0)); } if (o || r > 1) return a; throw y = !0, n; } return function (o, p, l) { if (f > 1) throw TypeError("Generator is already running"); for (y && 1 === p && d(p, l), c = p, u = l; (t = c < 2 ? e : u) || !y;) { i || (c ? c < 3 ? (c > 1 && (G.n = -1), d(c, u)) : G.n = u : G.v = u); try { if (f = 2, i) { if (c || (o = "next"), t = i[o]) { if (!(t = t.call(i, u))) throw TypeError("iterator result is not an object"); if (!t.done) return t; u = t.value, c < 2 && (c = 0); } else 1 === c && (t = i["return"]) && t.call(i), c < 2 && (u = TypeError("The iterator does not provide a '" + o + "' method"), c = 1); i = e; } else if ((t = (y = G.n < 0) ? u : r.call(n, G)) !== a) break; } catch (t) { i = e, c = 1, u = t; } finally { f = 1; } } return { value: t, done: y }; }; }(r, o, i), !0), u; } var a = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} t = Object.getPrototypeOf; var c = [][n] ? t(t([][n]())) : (_regeneratorDefine2(t = {}, n, function () { return this; }), t), u = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(c); function f(e) { return Object.setPrototypeOf ? Object.setPrototypeOf(e, GeneratorFunctionPrototype) : (e.__proto__ = GeneratorFunctionPrototype, _regeneratorDefine2(e, o, "GeneratorFunction")), e.prototype = Object.create(u), e; } return GeneratorFunction.prototype = GeneratorFunctionPrototype, _regeneratorDefine2(u, "constructor", GeneratorFunctionPrototype), _regeneratorDefine2(GeneratorFunctionPrototype, "constructor", GeneratorFunction), GeneratorFunction.displayName = "GeneratorFunction", _regeneratorDefine2(GeneratorFunctionPrototype, o, "GeneratorFunction"), _regeneratorDefine2(u), _regeneratorDefine2(u, o, "Generator"), _regeneratorDefine2(u, n, function () { return this; }), _regeneratorDefine2(u, "toString", function () { return "[object Generator]"; }), (_regenerator = function _regenerator() { return { w: i, m: f }; })(); }
function _regeneratorDefine2(e, r, n, t) { var i = Object.defineProperty; try { i({}, "", {}); } catch (e) { i = 0; } _regeneratorDefine2 = function _regeneratorDefine(e, r, n, t) { function o(r, n) { _regeneratorDefine2(e, r, function (e) { return this._invoke(r, n, e); }); } r ? i ? i(e, r, { value: n, enumerable: !t, configurable: !t, writable: !t }) : e[r] = n : (o("next", 0), o("throw", 1), o("return", 2)); }, _regeneratorDefine2(e, r, n, t); }
function asyncGeneratorStep(n, t, e, r, o, a, c) { try { var i = n[a](c), u = i.value; } catch (n) { return void e(n); } i.done ? t(u) : Promise.resolve(u).then(r, o); }
function _asyncToGenerator(n) { return function () { var t = this, e = arguments; return new Promise(function (r, o) { var a = n.apply(t, e); function _next(n) { asyncGeneratorStep(a, r, o, _next, _throw, "next", n); } function _throw(n) { asyncGeneratorStep(a, r, o, _next, _throw, "throw", n); } _next(void 0); }); }; }
function postJson(_x, _x2) {
  return _postJson.apply(this, arguments);
}
function _postJson() {
  _postJson = _asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee3(url, body) {
    var resp;
    return _regenerator().w(function (_context3) {
      while (1) switch (_context3.n) {
        case 0:
          _context3.n = 1;
          return fetch(url, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
          });
        case 1:
          resp = _context3.v;
          return _context3.a(2, resp.json());
      }
    }, _callee3);
  }));
  return _postJson.apply(this, arguments);
}
document.addEventListener('DOMContentLoaded', function () {
  // Interface switching elements
  var echoModeBtn = document.getElementById('echo-mode-btn');
  var computeModeBtn = document.getElementById('compute-mode-btn');
  var echoInterface = document.getElementById('echo-interface');
  var computeInterface = document.getElementById('compute-interface');

  // Function to clear all input fields (FR-003, FR-004)
  function clearAllFields() {
    // Clear Echo interface fields
    document.getElementById('enter-text').value = '';
    document.getElementById('echo-output').value = '';

    // Clear Compute interface fields
    document.getElementById('x').value = '';
    document.getElementById('y').value = '';
    document.getElementById('result').value = '';
  }

  // FR-003: Echo mode functionality
  echoModeBtn.addEventListener('click', function () {
    clearAllFields();
    echoInterface.style.display = 'block';
    computeInterface.style.display = 'none';
  });

  // FR-004: Compute mode functionality  
  computeModeBtn.addEventListener('click', function () {
    clearAllFields();
    echoInterface.style.display = 'none';
    computeInterface.style.display = 'block';
  });

  // Echo interface elements
  var echoBtn = document.getElementById('echo-btn');
  var echoInput = document.getElementById('enter-text');
  var echoOutput = document.getElementById('echo-output');
  echoBtn.addEventListener('click', /*#__PURE__*/_asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee() {
    var text, data, _data$result, _t;
    return _regenerator().w(function (_context) {
      while (1) switch (_context.p = _context.n) {
        case 0:
          text = (echoInput.value || '').trim();
          _context.p = 1;
          _context.n = 2;
          return postJson('/api/echo', {
            text: text
          });
        case 2:
          data = _context.v;
          // New API format: { success: boolean, result?: string, error?: string }
          if (data.success) {
            echoOutput.value = (_data$result = data.result) !== null && _data$result !== void 0 ? _data$result : '';
          } else {
            echoOutput.value = "Error: ".concat(data.error);
          }
          _context.n = 4;
          break;
        case 3:
          _context.p = 3;
          _t = _context.v;
          echoOutput.value = 'Error';
        case 4:
          return _context.a(2);
      }
    }, _callee, null, [[1, 3]]);
  })));
  var opButtons = document.querySelectorAll('.calc-buttons button');
  var xInput = document.getElementById('x');
  var yInput = document.getElementById('y');
  var resultOutput = document.getElementById('result');
  opButtons.forEach(function (btn) {
    btn.addEventListener('click', /*#__PURE__*/_asyncToGenerator(/*#__PURE__*/_regenerator().m(function _callee2() {
      var op, x, y, data, _data, _t2;
      return _regenerator().w(function (_context2) {
        while (1) switch (_context2.p = _context2.n) {
          case 0:
            op = btn.dataset.op;
            x = xInput.value.trim();
            y = yInput.value.trim();
            _context2.p = 1;
            if (!(op === 'add')) {
              _context2.n = 3;
              break;
            }
            _context2.n = 2;
            return postJson('/api/add', {
              x: x,
              y: y
            });
          case 2:
            data = _context2.v;
            if (data.success) {
              resultOutput.value = String(data.result);
            } else {
              resultOutput.value = "Error: ".concat(data.error);
            }
            _context2.n = 5;
            break;
          case 3:
            _context2.n = 4;
            return postJson('/api/calculate', {
              x: x,
              y: y,
              operation: op
            });
          case 4:
            _data = _context2.v;
            if (_data.success) {
              resultOutput.value = String(_data.result);
            } else {
              resultOutput.value = "Error: ".concat(_data.error);
            }
          case 5:
            _context2.n = 7;
            break;
          case 6:
            _context2.p = 6;
            _t2 = _context2.v;
            resultOutput.value = 'Error';
          case 7:
            return _context2.a(2);
        }
      }, _callee2, null, [[1, 6]]);
    })));
  });
});
