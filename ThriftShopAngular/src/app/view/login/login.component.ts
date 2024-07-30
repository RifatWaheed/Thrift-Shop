import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  loginTitle: string = "Sign in";
  userStateText: string = "New user? ";
  toggleTitle: string = "Sign up";
  isSignupClicked: boolean = false;

  passwordTextType: string = "password";
  confirmPasswordTextType: string = "password";
  isPasswordVisible: boolean = false;
  isConfirmPasswordVisible: boolean = false;

  isPasswordFocus: boolean = false;

  hintText: string = "Required 1 uppercase, 1 digit and 8 characters min";
  constructor() {

  }

  onSignupClicked() {
    if (!this.isSignupClicked) {
      this.isSignupClicked = true;
      this.loginTitle = "Sign up";
      this.userStateText = "Existing user? ";
      this.toggleTitle = "Sign in";
    }
    else {
      this.isSignupClicked = false;
      this.loginTitle = "Sign in";
      this.userStateText = "New user? ";
      this.toggleTitle = "Sign up";
    }
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
