import { Routes } from '@angular/router';
import { HomeComponent } from './view/home/home.component';
import { ContactComponent } from './view/contact/contact.component';
import { ProductsComponent } from './view/admin-panel/products/products.component';
import { AdminPanelComponent } from './view/admin-panel/admin-panel.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'adminPanel', component: AdminPanelComponent, },
  { path: 'adminPanel/products', component: ProductsComponent, },


];
