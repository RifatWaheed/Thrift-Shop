import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  loginTitle: string = "Login";
  userStateText: string = "New user? ";
  toggleTitle: string = "Sign up";
  isSignupClicked: boolean = false;

  passwordTextType: string = "password";
  confirmPasswordTextType: string = "password";
  isPasswordVisible: boolean = false;
  isConfirmPasswordVisible: boolean = false;

  isPasswordFocus: boolean = false;
  password : string = '';
  hintText: string = "Required 1 uppercase, 1 digit and 8 characters min";
  constructor() {

  }

  onSignupClicked() {
    if (!this.isSignupClicked) {
      this.isSignupClicked = true;
      this.isPasswordVisible = false;
      this.passwordTextType = "password";
      this.loginTitle = "Sign up";
      this.userStateText = "Existing user? ";
      this.toggleTitle = "Login";
    }
    else {
      this.isSignupClicked = false;
      this.isPasswordVisible = false;
      this.passwordTextType = "password"
      this.isConfirmPasswordVisible = false;
      this.loginTitle = "Login";
      this.userStateText = "New user? ";
      this.toggleTitle = "Sign up";
    }
    this.password  = '';
  }

  onShowPasswordClicked() {
    this.isPasswordVisible = true;
    this.passwordTextType = "text";
  }
  onHidePasswordClicked() {
    this.isPasswordVisible = false;
    this.passwordTextType = "password";
  }

  onShowConfirmPasswordClicked() {
    this.isConfirmPasswordVisible = true;
    this.confirmPasswordTextType = "text";
  }
  onHideConfirmPasswordClicked() {
    this.isConfirmPasswordVisible = false;
    this.confirmPasswordTextType = "password";
  }

  onPasswordFocus() {
    this.isPasswordFocus = true;
  }
  onPasswordBlur() {
    this.isPasswordFocus = false;
  }
}
