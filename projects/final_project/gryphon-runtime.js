(()=>{
const prefix='gryphon-app-local:v1:3b329a7a-0534-4d41-840e-4285b269c3b9:';
window.gryphon={storage:{
get:async key=>JSON.parse(localStorage.getItem(prefix+key)||'null'),
set:async(key,value)=>{localStorage.setItem(prefix+key,JSON.stringify(value));return value},
remove:async key=>{localStorage.removeItem(prefix+key)}}};
})();