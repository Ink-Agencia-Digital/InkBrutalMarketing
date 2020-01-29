<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Objetivos</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link :to="{ name: 'crear_proceso' }" class="btn btn-info">
                <i class="material-icons" style="color:white;">add</i>Crear
              </router-link>
            </li>
          </ul>
        </div>
        <div class=" body table-responsive">
          <table class="table">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Persona</th>
                <th scope="col">Etapa</th>
                <th scope="col">Idea</th>
                <th scope="col">Acción</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td><label class="" for="persona">Persona</label></td>
                <td><label class="" for="descripcion">Etapa</label></td>
                <td><label class="" for="medios">Idea</label></td>
                <td>
                  <router-link :to="{ name: 'proceso' }" class="bp btn-primary">
                    Modificar
                  </router-link>
                  <button type="button" class="bpn btn-danger">Eliminar</button>
                </td>
              </tr>
              <tr>
                <th scope="row">2</th>
                <td><label class="" for="persona">Persona</label></td>
                <td><label class="" for="descripcion">Etapa</label></td>
                <td><label class="" for="medios">Idea</label></td>
                <td>
                  <router-link :to="{ name: 'proceso' }" class="bp btn-primary">
                    Modificar
                  </router-link>
                  <button type="button" class="bpn btn-danger">Eliminar</button>
                </td>
              </tr>
              <tr>
                <th scope="row">3</th>
                <td><label class="" for="persona">Persona</label></td>
                <td><label class="" for="descripcion">Etapa</label></td>
                <td><label class="" for="medios">Idea</label></td>
                <td>
                  <router-link :to="{ name: 'proceso' }" class="bp btn-primary">
                    Modificar
                  </router-link>
                  <button type="button" class="bpn btn-danger">Eliminar</button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="my-4">
            <p v-show="loadingComportamientos">...Cargando...</p>
            <button
              v-show="nextComportamiento"
              @click="getComportamientos('MAS')"
              class="btn btn-sm btn-outline-success"
            >
              Cargar Más
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
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
