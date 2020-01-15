<template>
  <div id="app">
    <NavsComponent />
    <router-view />
  </div>
</template>
<script>
import NavsComponent from "./components/Navs";
export default {
  name: "App",
  components: {
    NavsComponent
  }
};
</script>
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;
}

.btn {
  left: 83%;
  text-align: center;
  border: 0px;
  position: relative;
  width: 120px;
  height: 39px;
}

.titulo {
  padding-left: 8%;
}

.botn {
  left: 43%;
  text-align: center;
  border: 0px;
  position: relative;
  width: 120px;
  height: 39px;
}

.a {
  left: 130px;
  text-align: center;
  border: 0px;
  position: relative;
  width: 120px;
  height: 39px;
  color: black;
}
</style>
