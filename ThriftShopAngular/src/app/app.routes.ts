import { Routes } from '@angular/router';
import { HomeComponent } from './view/home/home.component';
import { ContactComponent } from './view/contact/contact.component';

export const routes: Routes = [
    {path: '' , component: HomeComponent},
    {path: 'contact' , component: ContactComponent},

];
