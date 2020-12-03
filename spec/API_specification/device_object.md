(device-object)=

# Device object

> Array API specification for the device object.

A conforming implementation of the array API standard must provide and support a `device` object having the following attributes and methods adhering to the following conventions. 


## Methods

(method-__init__)=
### \_\_init\_\_(device_str, /)

#### Parameters

-   **device_str**: _str_

    -   device specification string, in the form `'type'` or `'type:index'`. See the `type` and `index` attributes for details.

#### Returns

-   **out**: _&lt;device&gt;_

    -   a device instance, identifying a hardware device.

## Attributes

<!-- NOTE: please keep the attributes in alphabetical order -->

(attribute-index)=
### index

Index of the device.

#### Returns

-   **out**: _Optional[int]_

    -   index of the device, if the device type supports multiple devices. `None` otherwise.

(attribute-str)=
### str

String representation of the device.

#### Returns

-   **out**: _str_

    -   device specification string, in the form `'type'` or `'type:index'`. See the `type` and `index` attributes for details.

(attribute-type)=
### type

#### Returns

-   **out**: _str_

    -   device type. Valid options are: `'cpu'`, `'gpu'`, `'tpu'`.
