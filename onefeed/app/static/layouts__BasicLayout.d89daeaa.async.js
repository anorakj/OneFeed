(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[0],{maEh:function(t,e,n){"use strict";n.r(e);var a=n("wx14"),r=n("KQm4"),c=n("Hx5s"),o=n("q1tI"),u=n.n(o),i=n("9kvl"),l=n("55Ip"),p=n("mxmt"),s=n.n(p),d=(n("+L6B"),n("2/Rp")),m=n("1OyB"),f=n("vuIU"),h=n("Ji7U"),b=n("LK+K"),g=n("o0o1"),v=n.n(g),w=n("HaE+"),O=n("t3Un");function j(){return y.apply(this,arguments)}function y(){return y=Object(w["a"])(v.a.mark((function t(){return v.a.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.abrupt("return",Object(O["a"])("/api/crawler/fetch",{method:"post"}));case 1:case"end":return t.stop()}}),t)}))),y.apply(this,arguments)}var E=function(t){Object(h["a"])(n,t);var e=Object(b["a"])(n);function n(){var t;Object(m["a"])(this,n);for(var a=arguments.length,r=new Array(a),c=0;c<a;c++)r[c]=arguments[c];return t=e.call.apply(e,[this].concat(r)),t.state={updating:!1},t.update=function(){t.setState((function(){return{updating:!0}})),j().then((function(){t.setState((function(){return{updating:!1}})),window.location.reload(!1)}))},t}return Object(f["a"])(n,[{key:"render",value:function(){var t=this,e=this.state.updating;return u.a.createElement(d["a"],{type:"primary",loading:e,onClick:function(){return t.update()}},"Update Now!")}}]),n}(o["Component"]),x=E,k=function(t){var e=t.dispatch,n=t.children,o=t.settings,p=function(t){e&&e({type:"global/changeLayoutCollapsed",payload:t})},d=Object(i["d"])(),m=d.formatMessage;return u.a.createElement(c["c"],Object(a["a"])({logo:s.a,formatMessage:m,menuHeaderRender:function(t,e){return u.a.createElement(l["a"],{to:"/"},t,e)},onCollapse:p,menuItemRender:function(t,e){return t.isUrl||t.children||!t.path?e:u.a.createElement(l["a"],{to:t.path},e)},breadcrumbRender:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];return[{path:"/",breadcrumbName:m({id:"menu.home"})}].concat(Object(r["a"])(t))},itemRender:function(t,e,n,a){var r=0===n.indexOf(t);return r?u.a.createElement(l["a"],{to:a.join("/")},t.breadcrumbName):u.a.createElement("span",null,t.breadcrumbName)},rightContentRender:function(){return u.a.createElement(x,null)}},t,o),n)};e["default"]=Object(i["a"])((function(t){var e=t.global,n=t.settings;return{collapsed:e.collapsed,settings:n}}))(k)},mxmt:function(t,e,n){t.exports=n.p+"static/logo.f0355d39.svg"}}]);