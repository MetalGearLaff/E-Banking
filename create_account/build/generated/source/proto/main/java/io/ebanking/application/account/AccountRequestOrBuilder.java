// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: account.proto

package io.ebanking.application.account;

public interface AccountRequestOrBuilder extends
    // @@protoc_insertion_point(interface_extends:account.AccountRequest)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>string email = 1;</code>
   * @return The email.
   */
  java.lang.String getEmail();
  /**
   * <code>string email = 1;</code>
   * @return The bytes for email.
   */
  com.google.protobuf.ByteString
      getEmailBytes();

  /**
   * <code>string account = 2;</code>
   * @return The account.
   */
  java.lang.String getAccount();
  /**
   * <code>string account = 2;</code>
   * @return The bytes for account.
   */
  com.google.protobuf.ByteString
      getAccountBytes();

  /**
   * <code>string password = 3;</code>
   * @return The password.
   */
  java.lang.String getPassword();
  /**
   * <code>string password = 3;</code>
   * @return The bytes for password.
   */
  com.google.protobuf.ByteString
      getPasswordBytes();
}