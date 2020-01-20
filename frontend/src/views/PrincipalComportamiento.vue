<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Comportamiento</h1>
      <br />
      <router-link :to="{ name: 'comportamiento' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Persona</th>
            <th scope="col">Descripción</th>
            <th scope="col">Medios</th>
            <th scope="col">Acción</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td><label class="" for="persona">Persona</label></td>
            <td><label class="" for="descripcion">Descripción</label></td>
            <td><label class="" for="medios">Medios</label></td>
            <td>
              <router-link
                :to="{ name: 'comportamiento' }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td><label class="" for="persona">Persona</label></td>
            <td><label class="" for="descripcion">Descripción</label></td>
            <td><label class="" for="medios">Medios</label></td>
            <td>
              <router-link
                :to="{ name: 'comportamiento' }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td><label class="" for="persona">Persona</label></td>
            <td><label class="" for="descripcion">Descripción</label></td>
            <td><label class="" for="medios">Medios</label></td>
            <td>
              <router-link
                :to="{ name: 'comportamiento' }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
    </div>
  </div>
</template>

<style>
.b {
  padding: 2% 3%;
  text-align: center;
  font-size: 16px;
  border-radius: 8px;
}
.bp {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
.bpn {
  padding: 2% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
