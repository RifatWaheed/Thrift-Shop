import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ContactInfoService {

  private contactInfoURL = 'http://127.0.0.1:8000/contactInfo'; // Replace with your API URL

  constructor(private http: HttpClient) { }

  getContactInfo(): Observable<any> {
    return this.http.get(this.contactInfoURL);
  }
}
