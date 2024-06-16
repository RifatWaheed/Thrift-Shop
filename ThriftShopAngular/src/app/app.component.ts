import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './view/navbar/navbar.component';
import { HomeComponent } from "./view/home/home.component";

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.scss',
    imports: [RouterOutlet, NavbarComponent, HomeComponent]
})
export class AppComponent {
  title = 'ThriftShopAngular';
}
