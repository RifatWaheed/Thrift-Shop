import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'https://api.example.com/contactInfo'; // Replace with your API URL

  constructor(private http: HttpClient) { }

  getData(): any {
    return this.http.get(this.apiUrl);
  }
}
