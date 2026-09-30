---
layout: page
title: Support
permalink: /support/
eyebrow: Help
lead: Answers to the most common questions about Loungemote, and how to reach us when you need a person.
description: Get help with Loungemote. Supported TVs, fixes for discovery, pairing and power-on problems, purchases and how to contact support.
---

<div class="contact-card">
  <div>
    <h2 id="contact">Contact us</h2>
    <p>Tell us your TV brand and model, and your iOS version. We answer by email.</p>
  </div>
  <a class="button button--ghost" href="mailto:{{ site.email }}">{% include icon.html name="mail" %}{{ site.email }}</a>
</div>

In the app, **Contact Support** writes this email for you and can attach a diagnostics file with private details removed.

## Supported devices

<ul class="device-table">
  {%- for p in site.data.platforms %}
  <li><strong>{{ p.name }}</strong><span>{{ p.detail }}</span></li>
  {%- endfor %}
</ul>

Philips TVs with Google TV connect as Google TV. Casting photos and videos works on every supported platform except Fire TV, and on Chromecast and DLNA devices. Apple TV is not supported.

Your iPhone and your TV must be on the same Wi-Fi network. Loungemote needs iOS 17 or iPadOS 17 or later.

## The app cannot find my TV

1. Make sure that the TV is on.
2. Connect your iPhone and your TV to the same Wi-Fi network. Guest networks often block the connection between devices.
3. Allow local network access. Open **Settings > Privacy & Security > Local Network** and turn on **Loungemote**.
4. On a Roku device, open **Settings > System > Advanced system settings > Control by mobile apps** and set **Network access** to **Default** or **Permissive**.
5. Close and open the app again. If the problem continues, restart the TV and your Wi-Fi router.

If the TV still does not appear, choose **Add by IP address** in the app and type the address from the TV's network settings.

## The TV asks me to allow the connection

The first time you connect, Samsung and LG TVs show a prompt on the screen. Select **Allow**. If you do not have the TV remote, use the buttons on the TV.

Android TV, Google TV, Fire TV, Vizio, Sony, Hisense and Philips Titan OS TVs show a code on the screen. Type this code in the app.

## The app cannot turn on my TV

Turn on the TV setting that lets the TV start from the network:

- **Samsung:** Power On with Mobile
- **LG:** Turn on via Wi-Fi, or Mobile TV On
- **Roku TV:** Fast TV start

The setting names and menu locations can be different on your TV model.

## Casting stops when I close the app

Photos and videos from your iPhone play from the app itself. Keep Loungemote open until the video ends. Links play from the internet, so the TV keeps playing them when you close the app.

## Restore purchases

In the app, open **Settings** and tap **Restore Purchases**. Use the same Apple Account that you used for the purchase.

## Cancel a subscription

Open **Settings > [your name] > Subscriptions** on your iPhone, then select **Loungemote**. See [Apple's instructions](https://support.apple.com/en-us/118428).

Apple handles all refunds. To ask for one, go to [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Privacy and terms

Loungemote collects no personal data. Read the [Privacy Policy]({{ '/privacy/' | relative_url }}) and the [Terms of Use]({{ '/terms/' | relative_url }}).

---

<small>{% include trademarks.html %}</small>
