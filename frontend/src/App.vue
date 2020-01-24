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
  position: relative;
  width: 100%;
  padding-right: 0px;
  padding-left: 250px;
}
</style>
