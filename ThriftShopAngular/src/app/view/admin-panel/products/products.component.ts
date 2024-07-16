import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { TitleComponent } from '../../title/title.component';
import { TableModule } from 'primeng/table';
import { ImportsModule } from '../../../../import/imports.module';
import { ButtonModule } from 'primeng/button';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabelModule } from 'primeng/floatlabel';
import { FormsModule } from '@angular/forms';
import { DropdownModule } from 'primeng/dropdown';
import { TagModule } from 'primeng/tag';
import { IconField, IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';
import { MultiSelectModule } from 'primeng/multiselect';
import { Product } from '../../../models/product/product';

interface City {
  name: string;
  code: string;
}

@Component({
  selector: 'products',
  standalone: true,
  imports: [TitleComponent, TableModule, CommonModule, RouterOutlet, RouterLink, RouterLinkActive, ButtonModule, InputTextModule, FloatLabelModule, FormsModule, DropdownModule, TagModule, IconFieldModule, InputIconModule, MultiSelectModule],
  templateUrl: './products.component.html',
  styleUrl: './products.component.scss'
})
export class ProductsComponent implements OnInit {

  dummProduct : Product = null

  value

  selectedProduct


  cities: City[] | undefined;

  selectedCity: City | undefined;


  products: any = [
    {
      id: '1000',
      code: 'f230fh0g3',
      name: 'Bamboo Watch',
      description: 'Product Description',
      image: 'bamboo-watch.jpg',
      price: 65,
      category: 'Accessories',
      quantity: 24,
      inventoryStatus: 'INSTOCK',
      rating: 5
    },
    {
      id: '1000',
      code: 'f230fh0g3',
      name: 'Bamboo Watch abcdrefefefefef',
      description: 'Product Description',
      image: 'bamboo-watch.jpg',
      price: 65,
      category: 'Accessories',
      quantity: 24,
      inventoryStatus: 'INSTOCK',
      rating: 5
    },
    {
      id: '1000',
      code: 'f230fh0g3',
      name: 'Bamboo Watch',
      description: 'Product Description',
      image: 'bamboo-watch.jpg',
      price: 65,
      category: 'Accessories',
      quantity: 24,
      inventoryStatus: 'INSTOCK',
      rating: 5
    }
  ]


  ngOnInit(): void {
    this.cities = [
      { name: 'New York', code: 'NY' },
      { name: 'Rome', code: 'RM' },
      { name: 'London', code: 'LDN' },
      { name: 'Istanbul', code: 'IST' },
      { name: 'Paris', code: 'PRS' }
    ];
  }


  onDropDownSelectionChange(){
    console.log(this.selectedProduct);
  }

  onEditButtonClick(data){
    console.log(data);
  }

  onDeleteButtonClick(data){
    console.log(data);
  }
}
