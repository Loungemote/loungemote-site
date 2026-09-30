---
layout: page
title: Privacy Policy
permalink: /privacy/
eyebrow: Legal
dated: true
lead: Loungemote is a TV remote for iPhone and iPad. This policy tells you which data the app uses and where that data goes.
description: Loungemote collects no personal data. It has no accounts, no analytics and no ads, and remote commands stay on your local network.
---

## Summary

<div class="summary" markdown="1">

- We do not collect personal data, and we do not sell or share it.
- The app has no user accounts.
- We do not operate servers for the app. The app communicates with the TVs and cast devices on your local network.
- The app does not contain analytics or advertising code, and it does not track you.
- When you cast to a Google Cast device, Google's Cast SDK sends diagnostic data that is not linked to you to Google. See [Casting](#casting).

</div>

In this policy, "the app" means the Loungemote app for iPhone and iPad, and "we" means the developer of Loungemote.

## Local network access

The app asks for Local Network permission. It uses this permission to:

- find TVs and streaming devices on your Wi-Fi network,
- send remote control commands to the TV that you select,
- turn on a TV with Wake-on-LAN, if you use this feature,
- send photos, videos and links that you choose to a TV or cast device.

Remote control commands stay on your local network, between your iPhone and your TV.

## Casting

When you cast a photo or video from your iPhone, the app serves that one file to the TV over your Wi-Fi network while it plays. The file is not uploaded anywhere. When you cast a link, the TV loads the link from the internet by itself.

Links you played recently and playlists you add are stored only on your iPhone. You can clear them in the app.

To cast to Chromecast and other Google Cast devices, the app uses Google's Cast SDK. The SDK starts only when you use casting. It sends Google diagnostic data, usage data about the cast session, a device identifier and a coarse location derived from your IP address. Google does not link this data to you, and it is not used for tracking. See [Google's privacy policy](https://policies.google.com/privacy).

## Data stored on your device

To reconnect to your TVs quickly, the app keeps this data on your iPhone:

- the name, model, platform, IP address and MAC address of each TV that you add,
- pairing data from the TV, for example an access token and a certificate fingerprint,
- for Android TV and Google TV, a security key and certificate that the app creates on your iPhone.

The app uses this data only to connect to your TVs. It does not send this data to us or to any third party.

The app keeps pairing data in the iOS Keychain. iOS can keep Keychain data after you delete an app. To delete the data for a TV, remove the TV in the app (**Settings > TVs > Forget This TV**).

## Support emails

If you choose **Contact Support** or **Report Problem** in the app, the app opens an email to us. It can attach a diagnostics file: the app version, iOS version, TV platforms and recent connection errors. The app removes IP addresses, MAC addresses, TV names and serial numbers from this file first. You see the email before you send it.

When you email us, we receive your email address and whatever you write. We use them only to answer you. You can ask us to delete your messages at any time.

## Purchases

Apple processes all payments. We do not receive your name, email address or payment details. The app receives transaction information from Apple, for example which product you bought and when your subscription renews. The app uses this information only to unlock paid features.

## Diagnostics from Apple

If you turn on **Share With App Developers** in iOS Settings, Apple can share crash reports and usage statistics with us. This data does not identify you. You control this setting in **Settings > Privacy & Security > Analytics & Improvements**.

## This website

This website has no cookies, no analytics and no advertising, and it loads nothing from other sites. It is hosted on GitHub Pages. Like every web host, GitHub receives technical data when you open a page, for example your IP address. See the [GitHub privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Your choices and rights

Because the app sends us no personal data, we hold nothing about you that we could show, correct, export or delete. The data the app uses is on your iPhone, and you control it:

- remove a TV in the app to delete its pairing data,
- clear recent links and playlists in the app,
- turn off Local Network access in **Settings > Privacy & Security > Local Network**,
- delete the app to remove its other data.

If you have emailed us, you can ask for a copy of that correspondence or ask us to delete it. Privacy laws in some places, for example the European Economic Area, the United Kingdom and California, give you further rights over personal data. To use them, email us.

## Children

The app is not directed to children under 13. We do not knowingly collect data from children.

## Changes to this policy

If we change how the app uses data, we will update this page and the effective date.

## Contact

If you have questions about this policy, email [{{ site.email }}](mailto:{{ site.email }}).
