You can use [GPG Suite for macOS](https://gpgtools.org) to generate the GPG key
with the settings listed in the exercise text. We recommend you install it
using [homebrew](https://brew.sh/)

`$ brew install gpgtools`

You can then open up the GPG Keychain application and generate a new GPG key
listing your name, KU e-mail address, the key type RSA, of length 4096, to
expire one year from now, with a passphrase.

You can then use the export function to export the public key to your GPG-keys
repository. (**Do not** include the secret key.)

This will create a .asc file rather than a .gpg file, as suggested in our guide.
The difference is that the former is a binary format, which can be hard to
handle: if you open a binary-file in a text-editor, all you see is gibberish.
The latter is an ASCII-based, so-called "armor" format, which can easier to
handle. For the purposes of this course, either format is fine.

To make GPG Keychain export keys in the ASCII armor format, you must first do
the following in your Terminal:

`$ defaults write org.gpgtools.gpgservices UseASCIIOutput -bool YES`

Restart GPG Keychain, an try exporting the file again. The filename extension
will still be .asc (you'll have to change that manually), but you can now open
the file in a text-editor, and see something like this:
```

    -----BEGIN PGP PUBLIC KEY BLOCK-----
    ...
    -----END PGP PUBLIC KEY BLOCK-----
```

By Oleks Shturmov
