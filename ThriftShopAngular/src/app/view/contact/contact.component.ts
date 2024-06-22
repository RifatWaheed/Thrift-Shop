import { Component, OnInit } from '@angular/core';
import { ContactInfoService } from '../../services/contactInfo.service';

@Component({
  selector: 'contact',
  standalone: true,
  imports: [],
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.scss'
})
export class ContactComponent implements OnInit {

  contactInfoResponse: any;
  contactInfoMessage: string = '';

  constructor(
    private contactInfoService: ContactInfoService,
  ) { }

  ngOnInit(): void {
    this.getContactInfo();
  }

  getContactInfo() {
    this.contactInfoService.getContactInfo().subscribe({
      next: (resp: any) => {
        this.contactInfoResponse = resp;
        this.contactInfoMessage = resp.message;
        console.log(resp);
      },
      error: (error: any) => {
        console.log(error);
      },
      complete: () => { },
    });

  }

}
